def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 91, "metric_value": 0.9747, "depth": 2}
		if obj[3]<=9:
			# {"feature": "Distance", "instances": 59, "metric_value": 0.8663, "depth": 3}
			if obj[7]>1:
				# {"feature": "Bar", "instances": 35, "metric_value": 0.9852, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 1.0, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Passanger", "instances": 17, "metric_value": 0.9367, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[2]<=0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]>0:
									return 'True'
								elif obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[2]>2:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[2]<=2:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[5]>1.0:
						# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[0]>2:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[0]<=2:
								return 'True'
							else: return 'True'
						elif obj[2]>2:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=0:
								return 'False'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[7]<=1:
				# {"feature": "Education", "instances": 24, "metric_value": 0.4138, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[0]>1:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=1.0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>1.0:
								return 'True'
							else: return 'True'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					elif obj[5]<=0.0:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>2.0:
							return 'True'
						elif obj[4]<=2.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>9:
			# {"feature": "Education", "instances": 32, "metric_value": 0.9544, "depth": 3}
			if obj[2]>0:
				# {"feature": "Bar", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.6723, "depth": 5}
					if obj[5]<=3.0:
						# {"feature": "Distance", "instances": 16, "metric_value": 0.5436, "depth": 6}
						if obj[7]>1:
							# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]<=1:
							return 'False'
						else: return 'False'
					elif obj[5]>3.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=1:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]>1:
								return 'False'
							else: return 'False'
						elif obj[4]>0.0:
							return 'False'
						else: return 'False'
					elif obj[5]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.9183, "depth": 2}
		if obj[5]<=2.0:
			# {"feature": "Bar", "instances": 32, "metric_value": 0.8571, "depth": 3}
			if obj[4]<=0.0:
				# {"feature": "Occupation", "instances": 19, "metric_value": 0.6292, "depth": 4}
				if obj[3]>0:
					# {"feature": "Education", "instances": 18, "metric_value": 0.5033, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[7]>1:
							# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[0]>2:
								return 'False'
							else: return 'False'
						elif obj[7]<=1:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]>0.0:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[7]<=2:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[3]<=10:
						# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[3]>10:
						return 'False'
					else: return 'False'
				elif obj[7]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>2.0:
			# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=14:
				return 'True'
			elif obj[3]>14:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
