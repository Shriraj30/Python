using Microsoft.AspNetCore.Mvc;
using LabourRegistration.Models;
using System.IO;
using System.Threading.Tasks;

namespace LabourRegistration.Controllers
{
    public class AccountController : Controller
    {
        [HttpGet]
        public IActionResult Register()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Register(RegisterViewModel model)
        {
            if (ModelState.IsValid)
            {
                if (model.Document != null)
                {
                    var filePath = Path.Combine("wwwroot", "documents", model.Document.FileName);
                    using (var stream = new FileStream(filePath, FileMode.Create))
                    {
                        await model.Document.CopyToAsync(stream);
                    }

                    return RedirectToAction("Success");
                }
                else
                {
                    ModelState.AddModelError("", "Please upload a document.");
                }
            }

            return View(model);
        }

        public IActionResult Success()
        {
            return View();
        }
    }
}

