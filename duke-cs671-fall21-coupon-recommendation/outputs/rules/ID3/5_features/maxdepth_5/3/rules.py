def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4716, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 5887, "metric_value": 0.4585, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Restaurant20to50", "instances": 5324, "metric_value": 0.4539, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Occupation", "instances": 3520, "metric_value": 0.4621, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 3475, "metric_value": 0.4641, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Education", "instances": 45, "metric_value": 0.2589, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>1.0:
				# {"feature": "Education", "instances": 1804, "metric_value": 0.4334, "depth": 4}
				if obj[1]>1:
					# {"feature": "Occupation", "instances": 1119, "metric_value": 0.4496, "depth": 5}
					if obj[2]<=19:
						return 'True'
					elif obj[2]>19:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Occupation", "instances": 685, "metric_value": 0.3999, "depth": 5}
					if obj[2]<=18:
						return 'True'
					elif obj[2]>18:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Education", "instances": 563, "metric_value": 0.4901, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Restaurant20to50", "instances": 513, "metric_value": 0.4882, "depth": 4}
				if obj[3]>-1.0:
					# {"feature": "Occupation", "instances": 510, "metric_value": 0.4892, "depth": 5}
					if obj[2]<=7.82156862745098:
						return 'False'
					elif obj[2]>7.82156862745098:
						return 'False'
					else: return 'False'
				elif obj[3]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Occupation", "instances": 50, "metric_value": 0.463, "depth": 4}
				if obj[2]<=11:
					# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.4846, "depth": 5}
					if obj[3]>-1.0:
						return 'True'
					elif obj[3]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>11:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.3111, "depth": 5}
					if obj[3]>0.0:
						return 'True'
					elif obj[3]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 2260, "metric_value": 0.4771, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Occupation", "instances": 1494, "metric_value": 0.4609, "depth": 3}
			if obj[2]>1.9106811377923965:
				# {"feature": "Education", "instances": 1245, "metric_value": 0.4716, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 799, "metric_value": 0.4576, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 446, "metric_value": 0.4954, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=1.9106811377923965:
				# {"feature": "Education", "instances": 249, "metric_value": 0.3785, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 227, "metric_value": 0.3618, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 22, "metric_value": 0.4817, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[3]>1.0:
			# {"feature": "Occupation", "instances": 766, "metric_value": 0.4961, "depth": 3}
			if obj[2]<=13.98018183142262:
				# {"feature": "Distance", "instances": 643, "metric_value": 0.4975, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Education", "instances": 527, "metric_value": 0.4987, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[4]>2:
					# {"feature": "Education", "instances": 116, "metric_value": 0.4822, "depth": 5}
					if obj[1]<=4:
						return 'False'
					elif obj[1]>4:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>13.98018183142262:
				# {"feature": "Education", "instances": 123, "metric_value": 0.4569, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 72, "metric_value": 0.4851, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 51, "metric_value": 0.3975, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
