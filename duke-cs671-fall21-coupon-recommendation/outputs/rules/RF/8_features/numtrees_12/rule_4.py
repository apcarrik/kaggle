def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Education", "instances": 71, "metric_value": 0.9826, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 44, "metric_value": 1.0, "depth": 3}
			if obj[3]<=20:
				# {"feature": "Coupon", "instances": 42, "metric_value": 0.9984, "depth": 4}
				if obj[1]>1:
					# {"feature": "Passanger", "instances": 34, "metric_value": 0.9774, "depth": 5}
					if obj[0]>0:
						# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.9673, "depth": 6}
						if obj[5]>-1.0:
							# {"feature": "Bar", "instances": 32, "metric_value": 0.9745, "depth": 7}
							if obj[4]<=1.0:
								# {"feature": "Direction_same", "instances": 16, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[4]>1.0:
								# {"feature": "Direction_same", "instances": 16, "metric_value": 0.896, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=3.0:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[0]<=2:
							return 'False'
						elif obj[0]>2:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0.0:
								return 'False'
							elif obj[4]>0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[5]>3.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>20:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Occupation", "instances": 27, "metric_value": 0.8767, "depth": 3}
			if obj[3]>1:
				# {"feature": "Passanger", "instances": 23, "metric_value": 0.7554, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[1]>2:
							# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[6]>0:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[5]>0.0:
									return 'False'
								elif obj[5]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[6]<=0:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[5]<=1.0:
									return 'True'
								elif obj[5]>1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=2:
							return 'True'
						else: return 'True'
					elif obj[4]>2.0:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[7]>2:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[3]>2:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[2]>0:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>0.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]<=2:
			return 'True'
		else: return 'True'
	else: return 'False'
