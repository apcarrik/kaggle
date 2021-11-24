def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9996, "depth": 1}
	if obj[7]>1:
		# {"feature": "Passanger", "instances": 74, "metric_value": 0.966, "depth": 2}
		if obj[0]>0:
			# {"feature": "Bar", "instances": 70, "metric_value": 0.9787, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Coupon", "instances": 60, "metric_value": 0.9481, "depth": 4}
				if obj[1]>1:
					# {"feature": "Occupation", "instances": 42, "metric_value": 0.9934, "depth": 5}
					if obj[3]<=11:
						# {"feature": "Education", "instances": 38, "metric_value": 1.0, "depth": 6}
						if obj[2]>0:
							# {"feature": "Direction_same", "instances": 30, "metric_value": 0.9871, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.999, "depth": 8}
								if obj[5]<=2.0:
									return 'False'
								elif obj[5]>2.0:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>11:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Occupation", "instances": 18, "metric_value": 0.65, "depth": 5}
					if obj[3]<=6:
						return 'False'
					elif obj[3]>6:
						# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]>2.0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[3]<=12:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>2.0:
							return 'True'
						elif obj[5]<=2.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]>12:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[7]<=1:
		# {"feature": "Coupon", "instances": 53, "metric_value": 0.9052, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 46, "metric_value": 0.8281, "depth": 3}
			if obj[3]<=11:
				# {"feature": "Education", "instances": 35, "metric_value": 0.5917, "depth": 4}
				if obj[2]>1:
					# {"feature": "Bar", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[5]>-1.0:
							# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[0]>0:
								# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[6]>0:
									return 'True'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[5]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Bar", "instances": 17, "metric_value": 0.3228, "depth": 5}
					if obj[4]<=1.0:
						return 'True'
					elif obj[4]>1.0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>0:
								return 'True'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>11:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[4]>1.0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>2.0:
							return 'False'
						elif obj[5]<=2.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]<=1.0:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>1:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=1:
									return 'True'
								else: return 'True'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[5]<=1.0:
				return 'False'
			elif obj[5]>1.0:
				# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>5:
					return 'True'
				elif obj[3]<=5:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'True'
