def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[3]>2:
		# {"feature": "Bar", "instances": 39, "metric_value": 0.9881, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Coupon", "instances": 21, "metric_value": 0.9587, "depth": 3}
			if obj[1]>1:
				# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[7]>1:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[5]>1.0:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[5]<=1.0:
							return 'True'
						else: return 'True'
					elif obj[7]<=1:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]<=1.0:
							return 'False'
						elif obj[5]>1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]>0:
							return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Education", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[2]<=4:
				# {"feature": "Coupon", "instances": 17, "metric_value": 0.6723, "depth": 4}
				if obj[1]>0:
					# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[5]>1.0:
									return 'False'
								elif obj[5]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[6]<=0:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=1.0:
									return 'True'
								elif obj[5]>1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[7]>2:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=2:
		# {"feature": "Bar", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[4]>-1.0:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]>0.0:
					return 'True'
				elif obj[5]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]<=-1.0:
			return 'False'
		else: return 'False'
	else: return 'True'
