# SOP — Payments Overview

## When to use
When customers ask about payment methods, how to pay by bank transfer, or have payment issues.

## Key references
- Payment methods, bank details, and troubleshooting: `data/payment_methods.json`
- Klarna-specific questions: `SOP-klarna.md`

---

## Available Payment Methods

| Method | How it works |
|---|---|
| Credit/debit card | Standard Shopify checkout |
| Shop Pay | Express checkout (Shopify) |
| Apple Pay / Google Pay | Express checkout |
| Klarna | Standard checkout only — see `SOP-klarna.md` |
| SEPA bank transfer | Manual process — see below |

## SEPA Bank Transfer

### Bank Details (from `data/payment_methods.json`)

| Field | Value |
|---|---|
| **Account holder** | Afterfade BV |
| **IBAN** | BE90 7380 5400 0932 |
| **BIC/SWIFT** | KREDBEBBXXX |
| **Bank** | KBC (Belgium) |

### Process

1. Customer requests to pay by bank transfer (email or WhatsApp).
2. Send the bank details above.
3. Customer must include their **order number** as the payment reference.
4. Order is shipped once payment is confirmed in the Afterfade bank account.
5. SEPA transfers typically take 1–3 business days.

### Response Template

#### English
> You can pay by bank transfer using the details below:
>
> **Account holder:** Afterfade BV  
> **IBAN:** BE90 7380 5400 0932  
> **BIC/SWIFT:** KREDBEBBXXX  
>
> Please include your **order number** as the payment reference. We'll ship your order as soon as the payment is received (typically 1–3 business days).

#### Spanish
> Puede realizar el pago por transferencia bancaria con los siguientes datos:
>
> **Titular:** Afterfade BV  
> **IBAN:** BE90 7380 5400 0932  
> **BIC/SWIFT:** KREDBEBBXXX  
>
> Por favor incluya su **número de pedido** como concepto de la transferencia. Enviaremos su pedido en cuanto confirmemos el pago (normalmente 1-3 días laborables).

#### French
> Vous pouvez payer par virement bancaire avec les coordonnées suivantes :
>
> **Titulaire :** Afterfade BV  
> **IBAN :** BE90 7380 5400 0932  
> **BIC/SWIFT :** KREDBEBBXXX  
>
> Veuillez indiquer votre **numéro de commande** comme référence de paiement. Nous expédierons votre commande dès réception du paiement (généralement 1 à 3 jours ouvrables).

#### German
> Sie können per Banküberweisung mit folgenden Daten bezahlen:
>
> **Kontoinhaber:** Afterfade BV  
> **IBAN:** BE90 7380 5400 0932  
> **BIC/SWIFT:** KREDBEBBXXX  
>
> Bitte geben Sie Ihre **Bestellnummer** als Zahlungsreferenz an. Wir versenden Ihre Bestellung, sobald der Eingang bestätigt ist (in der Regel 1–3 Werktage).

#### Dutch
> U kunt betalen per bankoverschrijving met de volgende gegevens:
>
> **Rekeninghouder:** Afterfade BV  
> **IBAN:** BE90 7380 5400 0932  
> **BIC/SWIFT:** KREDBEBBXXX  
>
> Vermeld uw **bestelnummer** als betalingsreferentie. We versturen uw bestelling zodra de betaling is ontvangen (doorgaans 1–3 werkdagen).

### Notes
- Bank transfers are manual — shipping is not automatic. Someone must confirm payment before the order is marked as fulfilled.
- Do not ship orders based on a promise to pay — only after funds are received.
- If a customer asks for an invoice with bank details, send the response template above.

---

## Related
- **data/payment_methods.json** — bank details and troubleshooting
- **data/contacts.json** — contact channels
- **SOP-klarna.md** — Klarna-specific questions and troubleshooting
- **SOP-returns-and-refunds.md** — refund process
- **SOP-checking-orders.md** — checking order status
