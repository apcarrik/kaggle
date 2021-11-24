def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[2]>6:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[3]>0.0:
				# {"feature": "Coupon", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=6:
			return 'True'
		else: return 'True'
	elif obj[1]>2:
		return 'False'
	else: return 'False'
