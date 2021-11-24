def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[16]<=0:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[10]<=6:
			# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[11]>0:
					return 'False'
				elif obj[11]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>6:
			return 'False'
		else: return 'False'
	elif obj[16]>0:
		return 'True'
	else: return 'True'
