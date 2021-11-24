def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9671, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 111, "metric_value": 0.9353, "depth": 2}
		if obj[2]<=7.990990990990991:
			# {"feature": "Restaurant20to50", "instances": 68, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Distance", "instances": 61, "metric_value": 0.8537, "depth": 4}
				if obj[4]>1:
					# {"feature": "Education", "instances": 36, "metric_value": 0.7107, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					# {"feature": "Education", "instances": 25, "metric_value": 0.971, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]>7.990990990990991:
			# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.9996, "depth": 3}
			if obj[3]>-1.0:
				# {"feature": "Education", "instances": 41, "metric_value": 0.9996, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 35, "metric_value": 0.9947, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]<=-1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[1]>0:
			# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[3]>0.0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[2]<=6:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[2]>6:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>2:
						return 'True'
					elif obj[4]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
