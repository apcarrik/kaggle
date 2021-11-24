def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Distance", "instances": 63, "metric_value": 0.9998, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Restaurant20to50", "instances": 59, "metric_value": 0.9981, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Education", "instances": 49, "metric_value": 0.9755, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Bar", "instances": 45, "metric_value": 0.9911, "depth": 5}
					if obj[4]>-1.0:
						# {"feature": "Occupation", "instances": 43, "metric_value": 0.9965, "depth": 6}
						if obj[3]>4:
							# {"feature": "Direction_same", "instances": 27, "metric_value": 0.951, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Coupon", "instances": 20, "metric_value": 0.8813, "depth": 8}
								if obj[1]>0:
									return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[1]>0:
									return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[3]<=4:
							# {"feature": "Coupon", "instances": 16, "metric_value": 0.9544, "depth": 7}
							if obj[1]>0:
								# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[5]<=0.0:
				# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[6]<=0:
					return 'False'
				elif obj[6]>0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=7:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]<=2.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[7]>2:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Education", "instances": 22, "metric_value": 0.5746, "depth": 2}
		if obj[2]<=2:
			return 'True'
		elif obj[2]>2:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=9:
						return 'False'
					elif obj[3]>9:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
