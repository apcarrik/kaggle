def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4744, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 5889, "metric_value": 0.4618, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Restaurant20to50", "instances": 5308, "metric_value": 0.4572, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Occupation", "instances": 3522, "metric_value": 0.4644, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 3477, "metric_value": 0.4668, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Education", "instances": 45, "metric_value": 0.2311, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>1.0:
				# {"feature": "Education", "instances": 1786, "metric_value": 0.4375, "depth": 4}
				if obj[1]>1:
					# {"feature": "Occupation", "instances": 1099, "metric_value": 0.4553, "depth": 5}
					if obj[2]<=19:
						return 'True'
					elif obj[2]>19:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Occupation", "instances": 687, "metric_value": 0.4011, "depth": 5}
					if obj[2]<=18:
						return 'True'
					elif obj[2]>18:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Education", "instances": 581, "metric_value": 0.4917, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 532, "metric_value": 0.4898, "depth": 4}
				if obj[2]<=7.648496240601504:
					# {"feature": "Restaurant20to50", "instances": 336, "metric_value": 0.4972, "depth": 5}
					if obj[3]>-1.0:
						return 'False'
					elif obj[3]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>7.648496240601504:
					# {"feature": "Restaurant20to50", "instances": 196, "metric_value": 0.4717, "depth": 5}
					if obj[3]>-1.0:
						return 'False'
					elif obj[3]<=-1.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Occupation", "instances": 49, "metric_value": 0.4463, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.4348, "depth": 5}
					if obj[3]<=3.0:
						return 'True'
					elif obj[3]>3.0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.3727, "depth": 5}
					if obj[3]<=2.0:
						return 'True'
					elif obj[3]>2.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 2258, "metric_value": 0.4816, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Occupation", "instances": 1494, "metric_value": 0.4693, "depth": 3}
			if obj[2]>1.943768255746133:
				# {"feature": "Education", "instances": 1245, "metric_value": 0.4771, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 810, "metric_value": 0.4654, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 435, "metric_value": 0.4967, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=1.943768255746133:
				# {"feature": "Education", "instances": 249, "metric_value": 0.3992, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 229, "metric_value": 0.3882, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 20, "metric_value": 0.45, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>1.0:
			# {"feature": "Occupation", "instances": 764, "metric_value": 0.4913, "depth": 3}
			if obj[2]<=13.710484759667237:
				# {"feature": "Distance", "instances": 649, "metric_value": 0.4907, "depth": 4}
				if obj[4]>1:
					# {"feature": "Education", "instances": 414, "metric_value": 0.4907, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					# {"feature": "Education", "instances": 235, "metric_value": 0.4817, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]>13.710484759667237:
				# {"feature": "Education", "instances": 115, "metric_value": 0.4362, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 66, "metric_value": 0.4488, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 49, "metric_value": 0.3895, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
