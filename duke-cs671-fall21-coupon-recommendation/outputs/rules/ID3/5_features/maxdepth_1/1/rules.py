def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4722, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 5903, "metric_value": 0.4599, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Restaurant20to50", "instances": 5355, "metric_value": 0.4555, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Occupation", "instances": 3552, "metric_value": 0.4632, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 3508, "metric_value": 0.4649, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Education", "instances": 44, "metric_value": 0.2332, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>1.0:
				# {"feature": "Education", "instances": 1803, "metric_value": 0.4356, "depth": 4}
				if obj[1]>1:
					# {"feature": "Occupation", "instances": 1112, "metric_value": 0.4511, "depth": 5}
					if obj[2]<=19:
						return 'True'
					elif obj[2]>19:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Occupation", "instances": 691, "metric_value": 0.404, "depth": 5}
					if obj[2]<=18:
						return 'True'
					elif obj[2]>18:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Education", "instances": 548, "metric_value": 0.4922, "depth": 3}
			if obj[1]<=4:
				# {"feature": "Restaurant20to50", "instances": 545, "metric_value": 0.4927, "depth": 4}
				if obj[3]>-1.0:
					# {"feature": "Occupation", "instances": 542, "metric_value": 0.4941, "depth": 5}
					if obj[2]<=7.586715867158672:
						return 'False'
					elif obj[2]>7.586715867158672:
						return 'False'
					else: return 'False'
				elif obj[3]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 2244, "metric_value": 0.4761, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Education", "instances": 1483, "metric_value": 0.4612, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 938, "metric_value": 0.4448, "depth": 4}
				if obj[2]<=19.108887169188915:
					# {"feature": "Distance", "instances": 893, "metric_value": 0.449, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[2]>19.108887169188915:
					# {"feature": "Distance", "instances": 45, "metric_value": 0.342, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Occupation", "instances": 545, "metric_value": 0.4774, "depth": 4}
				if obj[2]>1.391821210055043:
					# {"feature": "Distance", "instances": 440, "metric_value": 0.4955, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]<=1.391821210055043:
					# {"feature": "Distance", "instances": 105, "metric_value": 0.394, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]>1.0:
			# {"feature": "Occupation", "instances": 761, "metric_value": 0.4916, "depth": 3}
			if obj[2]<=13.94152603856423:
				# {"feature": "Distance", "instances": 642, "metric_value": 0.4962, "depth": 4}
				if obj[4]>1:
					# {"feature": "Education", "instances": 425, "metric_value": 0.4939, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					# {"feature": "Education", "instances": 217, "metric_value": 0.4887, "depth": 5}
					if obj[1]<=4:
						return 'True'
					elif obj[1]>4:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]>13.94152603856423:
				# {"feature": "Education", "instances": 119, "metric_value": 0.4224, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 64, "metric_value": 0.4866, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 55, "metric_value": 0.3335, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
