def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[3]>0.0:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.9957, "depth": 2}
		if obj[2]<=5:
			# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[0]<=3:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>3:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]>2:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]>5:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[4]>1:
					# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]<=0.0:
		# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=4:
				return 'False'
			elif obj[2]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
