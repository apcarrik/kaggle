def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 5092, "metric_value": 0.4737, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 3670, "metric_value": 0.4624, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Restaurant20to50", "instances": 3294, "metric_value": 0.4578, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Occupation", "instances": 2156, "metric_value": 0.4665, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 2128, "metric_value": 0.4685, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Education", "instances": 28, "metric_value": 0.2917, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>1.0:
				# {"feature": "Education", "instances": 1138, "metric_value": 0.4351, "depth": 4}
				if obj[1]>0:
					# {"feature": "Occupation", "instances": 813, "metric_value": 0.4564, "depth": 5}
					if obj[2]<=18.46170992375947:
						return 'True'
					elif obj[2]>18.46170992375947:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Occupation", "instances": 325, "metric_value": 0.3733, "depth": 5}
					if obj[2]>2:
						return 'True'
					elif obj[2]<=2:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Education", "instances": 376, "metric_value": 0.4882, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 261, "metric_value": 0.4811, "depth": 4}
				if obj[2]<=19.732567148138145:
					# {"feature": "Restaurant20to50", "instances": 240, "metric_value": 0.4845, "depth": 5}
					if obj[3]>-1.0:
						return 'False'
					elif obj[3]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>19.732567148138145:
					# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.3697, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Occupation", "instances": 115, "metric_value": 0.4882, "depth": 4}
				if obj[2]<=21:
					# {"feature": "Restaurant20to50", "instances": 113, "metric_value": 0.4863, "depth": 5}
					if obj[3]<=3.0:
						return 'True'
					elif obj[3]>3.0:
						return 'False'
					else: return 'False'
				elif obj[2]>21:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 1422, "metric_value": 0.4738, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Occupation", "instances": 933, "metric_value": 0.4535, "depth": 3}
			if obj[2]>2.029621736825855:
				# {"feature": "Education", "instances": 741, "metric_value": 0.4731, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 475, "metric_value": 0.4629, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 266, "metric_value": 0.489, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=2.029621736825855:
				# {"feature": "Education", "instances": 192, "metric_value": 0.3484, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 177, "metric_value": 0.3343, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.4286, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[3]>1.0:
			# {"feature": "Distance", "instances": 489, "metric_value": 0.4964, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Occupation", "instances": 398, "metric_value": 0.4949, "depth": 4}
				if obj[2]>2.1810206157307244:
					# {"feature": "Education", "instances": 319, "metric_value": 0.4924, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]<=2.1810206157307244:
					# {"feature": "Education", "instances": 79, "metric_value": 0.476, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>2:
				# {"feature": "Occupation", "instances": 91, "metric_value": 0.4825, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 90, "metric_value": 0.4839, "depth": 5}
					if obj[1]<=4:
						return 'False'
					elif obj[1]>4:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
