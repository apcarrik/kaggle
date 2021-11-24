def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4734, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 5886, "metric_value": 0.4619, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Restaurant20to50", "instances": 5298, "metric_value": 0.4572, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Occupation", "instances": 3513, "metric_value": 0.4652, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 3464, "metric_value": 0.4675, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Education", "instances": 49, "metric_value": 0.244, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>1.0:
				# {"feature": "Education", "instances": 1785, "metric_value": 0.4347, "depth": 4}
				if obj[1]>1:
					# {"feature": "Occupation", "instances": 1102, "metric_value": 0.4578, "depth": 5}
					if obj[2]<=19:
						return 'True'
					elif obj[2]>19:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Occupation", "instances": 683, "metric_value": 0.3916, "depth": 5}
					if obj[2]<=18:
						return 'True'
					elif obj[2]>18:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Education", "instances": 588, "metric_value": 0.4927, "depth": 3}
			if obj[1]<=4:
				# {"feature": "Restaurant20to50", "instances": 585, "metric_value": 0.4931, "depth": 4}
				if obj[3]<=3.0:
					# {"feature": "Occupation", "instances": 575, "metric_value": 0.495, "depth": 5}
					if obj[2]<=7.471304347826087:
						return 'False'
					elif obj[2]>7.471304347826087:
						return 'False'
					else: return 'False'
				elif obj[3]>3.0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.1778, "depth": 5}
					if obj[2]<=14:
						return 'False'
					elif obj[2]>14:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 2261, "metric_value": 0.4788, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Occupation", "instances": 1485, "metric_value": 0.4646, "depth": 3}
			if obj[2]>1.992379689589069:
				# {"feature": "Education", "instances": 1244, "metric_value": 0.4728, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 814, "metric_value": 0.4596, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 430, "metric_value": 0.4937, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=1.992379689589069:
				# {"feature": "Education", "instances": 241, "metric_value": 0.3946, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 217, "metric_value": 0.3787, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 24, "metric_value": 0.475, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>1.0:
			# {"feature": "Occupation", "instances": 776, "metric_value": 0.4922, "depth": 3}
			if obj[2]<=8.108247422680412:
				# {"feature": "Distance", "instances": 472, "metric_value": 0.4901, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Education", "instances": 385, "metric_value": 0.497, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					# {"feature": "Education", "instances": 87, "metric_value": 0.4365, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>8.108247422680412:
				# {"feature": "Education", "instances": 304, "metric_value": 0.4779, "depth": 4}
				if obj[1]>1:
					# {"feature": "Distance", "instances": 187, "metric_value": 0.4958, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Distance", "instances": 117, "metric_value": 0.4426, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
