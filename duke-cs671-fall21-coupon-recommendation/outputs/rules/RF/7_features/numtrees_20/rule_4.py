def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[6]<=2:
		# {"feature": "Coupon", "instances": 48, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.7706, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Education", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>5:
							return 'False'
						elif obj[3]<=5:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]>1:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>1.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[3]<=14:
					return 'True'
				elif obj[3]>14:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Direction_same", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[3]>4:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]<=4:
					# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=1.0:
								return 'True'
							elif obj[4]>1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]>2:
		return 'False'
	else: return 'False'
