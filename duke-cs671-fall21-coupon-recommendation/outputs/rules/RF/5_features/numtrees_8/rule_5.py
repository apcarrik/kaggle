def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 110, "metric_value": 0.9883, "depth": 2}
		if obj[2]>1.8860688554692944:
			# {"feature": "Education", "instances": 92, "metric_value": 0.9986, "depth": 3}
			if obj[1]>1:
				# {"feature": "Restaurant20to50", "instances": 54, "metric_value": 0.9841, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Distance", "instances": 36, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]>1.0:
					# {"feature": "Distance", "instances": 18, "metric_value": 0.9641, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.9268, "depth": 4}
				if obj[3]<=3.0:
					# {"feature": "Distance", "instances": 37, "metric_value": 0.9353, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]>3.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=1.8860688554692944:
			# {"feature": "Education", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[3]>1.0:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[2]<=20:
			# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[1]<=3:
					return 'False'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>1.0:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>20:
			return 'True'
		else: return 'True'
	else: return 'False'
