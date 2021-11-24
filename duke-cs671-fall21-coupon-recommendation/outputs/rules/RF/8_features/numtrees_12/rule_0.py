def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[1]>1:
		# {"feature": "Restaurant20to50", "instances": 62, "metric_value": 0.9236, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Occupation", "instances": 42, "metric_value": 0.9852, "depth": 3}
			if obj[3]<=20:
				# {"feature": "Education", "instances": 41, "metric_value": 0.9789, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Bar", "instances": 35, "metric_value": 0.9947, "depth": 5}
					if obj[4]<=3.0:
						# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 25, "metric_value": 0.9988, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 14, "metric_value": 0.9852, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[7]<=1:
									return 'False'
								elif obj[7]>1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[0]>1:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>3.0:
						return 'True'
					else: return 'True'
				elif obj[2]>2:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]>1:
						# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=1:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>1:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>20:
				return 'False'
			else: return 'False'
		elif obj[5]>1.0:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.6098, "depth": 3}
			if obj[3]<=12:
				# {"feature": "Distance", "instances": 19, "metric_value": 0.4855, "depth": 4}
				if obj[7]>1:
					# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]>2:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[4]>2.0:
						return 'False'
					else: return 'False'
				elif obj[7]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]>12:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Bar", "instances": 23, "metric_value": 0.6666, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=12:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[5]>1.0:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=2:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]>2:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[5]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[3]>12:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		elif obj[4]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
