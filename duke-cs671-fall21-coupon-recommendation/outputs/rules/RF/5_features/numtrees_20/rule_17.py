def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]<=15:
		# {"feature": "Coupon", "instances": 44, "metric_value": 0.994, "depth": 2}
		if obj[0]>1:
			# {"feature": "Distance", "instances": 31, "metric_value": 0.9383, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.8555, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>1.0:
					return 'True'
				else: return 'True'
			elif obj[4]>2:
				# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>1.0:
						return 'False'
					elif obj[3]<=1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]>1.0:
					# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>15:
		return 'False'
	else: return 'False'
