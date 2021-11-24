def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[11]<=4:
		# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9612, "depth": 2}
		if obj[13]>1.0:
			# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[12]<=3.0:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[17]<=2:
					return 'True'
				elif obj[17]>2:
					return 'False'
				else: return 'False'
			elif obj[12]>3.0:
				return 'False'
			else: return 'False'
		elif obj[13]<=1.0:
			return 'False'
		else: return 'False'
	elif obj[11]>4:
		return 'True'
	else: return 'True'
