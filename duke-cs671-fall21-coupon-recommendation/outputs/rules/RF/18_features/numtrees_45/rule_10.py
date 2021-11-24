def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[13]<=2.0:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Weather", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[7]<=1:
					return 'True'
				elif obj[7]>1:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		elif obj[3]>3:
			return 'False'
		else: return 'False'
	elif obj[13]>2.0:
		return 'True'
	else: return 'True'
