window.FORSHOR_SITE = {
    companyPhoneDisplay: "(801) 487-1656",
    companyPhoneHref: "tel:+18014871656"
};

document.addEventListener("DOMContentLoaded", function () {
    var site = window.FORSHOR_SITE || {};
    var companyPhoneDisplay = site.companyPhoneDisplay || "";
    var companyPhoneHref = site.companyPhoneHref || "";

    document.querySelectorAll("[data-company-phone-link]").forEach(function (link) {
        if (companyPhoneHref) {
            link.setAttribute("href", companyPhoneHref);
        }
    });

    document.querySelectorAll("[data-company-phone-display]").forEach(function (node) {
        node.textContent = companyPhoneDisplay;
    });
});
