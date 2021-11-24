def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[2]>1:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[3]>1.0:
						return 'True'
					elif obj[3]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[4]>1:
			return 'False'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
