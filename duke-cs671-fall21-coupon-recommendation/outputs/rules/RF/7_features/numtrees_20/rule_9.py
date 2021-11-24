def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[6]<=2:
		# {"feature": "Coupon", "instances": 44, "metric_value": 0.9865, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 33, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=6:
				# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Passanger", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[0]>0:
						# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=1:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[2]>1:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>6:
				# {"feature": "Passanger", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[3]>9:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=9:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]>2:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
