def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[9]<=1:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[5]<=2:
			# {"feature": "Income", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[13]>2:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[17]>0.0:
					return 'False'
				elif obj[17]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[13]<=2:
				return 'True'
			else: return 'True'
		elif obj[5]>2:
			return 'True'
		else: return 'True'
	elif obj[9]>1:
		return 'False'
	else: return 'False'
