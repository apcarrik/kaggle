def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 8148, "metric_value": 0.4751, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 5867, "metric_value": 0.4642, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Occupation", "instances": 5275, "metric_value": 0.46, "depth": 3}
			if obj[2]>0:
				# {"feature": "Restaurant20to50", "instances": 5219, "metric_value": 0.4609, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Education", "instances": 3452, "metric_value": 0.4675, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[3]>1.0:
					# {"feature": "Education", "instances": 1767, "metric_value": 0.4424, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Restaurant20to50", "instances": 56, "metric_value": 0.302, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Education", "instances": 41, "metric_value": 0.2498, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				elif obj[3]>1.0:
					# {"feature": "Education", "instances": 15, "metric_value": 0.4444, "depth": 5}
					if obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Education", "instances": 592, "metric_value": 0.4879, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 407, "metric_value": 0.4814, "depth": 4}
				if obj[3]>-1.0:
					# {"feature": "Occupation", "instances": 403, "metric_value": 0.4844, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Restaurant20to50", "instances": 185, "metric_value": 0.4854, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Occupation", "instances": 137, "metric_value": 0.4923, "depth": 5}
					if obj[2]>5:
						return 'True'
					elif obj[2]<=5:
						return 'False'
					else: return 'False'
				elif obj[3]>1.0:
					# {"feature": "Occupation", "instances": 48, "metric_value": 0.4058, "depth": 5}
					if obj[2]<=18:
						return 'True'
					elif obj[2]>18:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 2281, "metric_value": 0.4762, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Occupation", "instances": 1500, "metric_value": 0.459, "depth": 3}
			if obj[2]>1.9904707123952177:
				# {"feature": "Education", "instances": 1255, "metric_value": 0.4723, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 822, "metric_value": 0.46, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 433, "metric_value": 0.4929, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=1.9904707123952177:
				# {"feature": "Education", "instances": 245, "metric_value": 0.3628, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 225, "metric_value": 0.3489, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 20, "metric_value": 0.48, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>1.0:
			# {"feature": "Distance", "instances": 781, "metric_value": 0.4943, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Education", "instances": 641, "metric_value": 0.4917, "depth": 4}
				if obj[1]>0:
					# {"feature": "Occupation", "instances": 442, "metric_value": 0.498, "depth": 5}
					if obj[2]<=19.17084245775628:
						return 'True'
					elif obj[2]>19.17084245775628:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Occupation", "instances": 199, "metric_value": 0.4602, "depth": 5}
					if obj[2]<=9:
						return 'True'
					elif obj[2]>9:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>2:
				# {"feature": "Occupation", "instances": 140, "metric_value": 0.4823, "depth": 4}
				if obj[2]<=8.228571428571428:
					# {"feature": "Education", "instances": 82, "metric_value": 0.4571, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[2]>8.228571428571428:
					# {"feature": "Education", "instances": 58, "metric_value": 0.469, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
