def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=14:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]>1.0:
						return 'False'
					elif obj[3]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[3]<=3.0:
				return 'False'
			elif obj[3]>3.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>14:
		return 'True'
	else: return 'True'
