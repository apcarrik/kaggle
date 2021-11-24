def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Education", "instances": 20, "metric_value": 0.9341, "depth": 1}
	if obj[11]>0:
		# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.9799, "depth": 2}
		if obj[9]<=1:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[14]<=1.0:
					return 'True'
				elif obj[14]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>1:
			return 'True'
		else: return 'True'
	elif obj[11]<=0:
		return 'True'
	else: return 'True'
