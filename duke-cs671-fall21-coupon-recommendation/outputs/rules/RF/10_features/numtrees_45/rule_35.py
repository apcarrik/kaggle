def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[4]<=14:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]>0.0:
						return 'True'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>2.0:
				return 'False'
			else: return 'False'
		elif obj[4]>14:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[4]<=7:
			return 'False'
		elif obj[4]>7:
			# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
