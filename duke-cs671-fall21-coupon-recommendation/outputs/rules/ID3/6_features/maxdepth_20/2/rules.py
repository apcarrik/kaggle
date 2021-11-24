def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.9867, "depth": 1}
	if obj[1]>1:
		# {"feature": "Distance", "instances": 5886, "metric_value": 0.954, "depth": 2}
		if obj[5]<=2:
			# {"feature": "Passanger", "instances": 5298, "metric_value": 0.9388, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Restaurant20to50", "instances": 3502, "metric_value": 0.9635, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Occupation", "instances": 2300, "metric_value": 0.9739, "depth": 5}
					if obj[3]>0:
						# {"feature": "Education", "instances": 2269, "metric_value": 0.9757, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Education", "instances": 31, "metric_value": 0.6374, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Education", "instances": 1202, "metric_value": 0.9387, "depth": 5}
					if obj[2]>1:
						# {"feature": "Occupation", "instances": 746, "metric_value": 0.9657, "depth": 6}
						if obj[3]<=16:
							return 'True'
						elif obj[3]>16:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Occupation", "instances": 456, "metric_value": 0.8764, "depth": 6}
						if obj[3]<=18:
							return 'True'
						elif obj[3]>18:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 1796, "metric_value": 0.871, "depth": 4}
				if obj[3]>0:
					# {"feature": "Restaurant20to50", "instances": 1772, "metric_value": 0.8739, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Education", "instances": 1195, "metric_value": 0.8918, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						# {"feature": "Education", "instances": 577, "metric_value": 0.8319, "depth": 6}
						if obj[2]>1:
							return 'True'
						elif obj[2]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=0:
					# {"feature": "Education", "instances": 24, "metric_value": 0.5436, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.5917, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[5]>2:
			# {"feature": "Passanger", "instances": 588, "metric_value": 0.9939, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 570, "metric_value": 0.9897, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Restaurant20to50", "instances": 567, "metric_value": 0.9887, "depth": 5}
					if obj[4]<=3.0:
						# {"feature": "Occupation", "instances": 557, "metric_value": 0.9902, "depth": 6}
						if obj[3]>1.7716165352188504:
							return 'False'
						elif obj[3]<=1.7716165352188504:
							return 'False'
						else: return 'False'
					elif obj[4]>3.0:
						# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[3]<=14:
							return 'False'
						elif obj[3]>14:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Occupation", "instances": 18, "metric_value": 0.5033, "depth": 4}
				if obj[3]<=9:
					# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[4]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[3]>9:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Restaurant20to50", "instances": 2261, "metric_value": 0.9801, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Passanger", "instances": 1485, "metric_value": 0.953, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 1275, "metric_value": 0.9339, "depth": 4}
				if obj[3]>2.014390800020979:
					# {"feature": "Education", "instances": 1007, "metric_value": 0.9517, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 668, "metric_value": 0.9173, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 339, "metric_value": 0.9923, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=2.014390800020979:
					# {"feature": "Education", "instances": 268, "metric_value": 0.8395, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Distance", "instances": 241, "metric_value": 0.7961, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[2]>3:
						# {"feature": "Distance", "instances": 27, "metric_value": 0.999, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 210, "metric_value": 0.9994, "depth": 4}
				if obj[3]<=7.109523809523809:
					# {"feature": "Education", "instances": 141, "metric_value": 0.9895, "depth": 5}
					if obj[2]>1:
						# {"feature": "Distance", "instances": 73, "metric_value": 0.9999, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Distance", "instances": 68, "metric_value": 0.9597, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]>7.109523809523809:
					# {"feature": "Education", "instances": 69, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 54, "metric_value": 0.9641, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						# {"feature": "Distance", "instances": 15, "metric_value": 0.5665, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>1.0:
			# {"feature": "Occupation", "instances": 776, "metric_value": 1.0, "depth": 3}
			if obj[3]<=8.108247422680412:
				# {"feature": "Passanger", "instances": 472, "metric_value": 0.9931, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Distance", "instances": 401, "metric_value": 0.9854, "depth": 5}
					if obj[5]>1:
						# {"feature": "Education", "instances": 258, "metric_value": 0.9682, "depth": 6}
						if obj[2]<=3:
							return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						# {"feature": "Education", "instances": 143, "metric_value": 0.9997, "depth": 6}
						if obj[2]>1:
							return 'True'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 71, "metric_value": 0.9826, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 50, "metric_value": 0.9988, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 21, "metric_value": 0.8631, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>8.108247422680412:
				# {"feature": "Education", "instances": 304, "metric_value": 0.9819, "depth": 4}
				if obj[2]>1:
					# {"feature": "Distance", "instances": 187, "metric_value": 0.9983, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Passanger", "instances": 149, "metric_value": 0.9945, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						# {"feature": "Passanger", "instances": 38, "metric_value": 0.992, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=1:
					# {"feature": "Passanger", "instances": 117, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Distance", "instances": 100, "metric_value": 0.9507, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.5226, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
