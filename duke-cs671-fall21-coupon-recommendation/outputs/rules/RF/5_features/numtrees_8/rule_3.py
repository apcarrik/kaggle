def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 102, "metric_value": 0.9822, "depth": 2}
		if obj[2]<=17.258808055341447:
			# {"feature": "Distance", "instances": 96, "metric_value": 0.9685, "depth": 3}
			if obj[4]>1:
				# {"feature": "Restaurant20to50", "instances": 54, "metric_value": 0.999, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Education", "instances": 47, "metric_value": 0.9971, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[3]<=0.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.8631, "depth": 4}
				if obj[3]<=3.0:
					# {"feature": "Education", "instances": 40, "metric_value": 0.8813, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[3]>3.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]>17.258808055341447:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 25, "metric_value": 0.8555, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.9341, "depth": 3}
			if obj[2]<=12:
				# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.8997, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]>1.0:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>12:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
