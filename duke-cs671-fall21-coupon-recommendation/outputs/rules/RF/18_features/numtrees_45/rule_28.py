def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[11]>2:
		# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 1.0, "depth": 2}
		if obj[15]<=1.0:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[10]<=7:
				# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[14]<=2.0:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[13]>2.0:
						return 'False'
					elif obj[13]<=2.0:
						return 'True'
					else: return 'True'
				elif obj[14]>2.0:
					return 'True'
				else: return 'True'
			elif obj[10]>7:
				return 'False'
			else: return 'False'
		elif obj[15]>1.0:
			return 'True'
		else: return 'True'
	elif obj[11]<=2:
		return 'False'
	else: return 'False'
