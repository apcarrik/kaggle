def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.874, "depth": 1}
	if obj[2]<=12:
		# {"feature": "Education", "instances": 30, "metric_value": 0.9183, "depth": 2}
		if obj[1]>0:
			# {"feature": "Distance", "instances": 18, "metric_value": 0.9911, "depth": 3}
			if obj[4]>1:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[0]<=3:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]>0.0:
						return 'True'
					elif obj[3]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[0]>3:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]<=0.0:
						return 'True'
					elif obj[3]>0.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]>2:
					return 'False'
				elif obj[0]<=2:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=-1.0:
						return 'False'
					elif obj[3]>-1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>1:
					return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]>12:
		return 'True'
	else: return 'True'
