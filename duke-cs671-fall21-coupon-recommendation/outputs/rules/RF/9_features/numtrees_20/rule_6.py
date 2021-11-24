def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Time", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 28, "metric_value": 0.9963, "depth": 3}
			if obj[4]>4:
				# {"feature": "Education", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[5]>0.0:
						return 'False'
					elif obj[5]<=0.0:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[8]>1:
							return 'False'
						elif obj[8]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=0:
					# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[5]>0.0:
						return 'True'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=4:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[2]>0:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=0:
								return 'False'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							return 'True'
						else: return 'True'
					elif obj[5]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Education", "instances": 20, "metric_value": 0.6098, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Coupon", "instances": 18, "metric_value": 0.3095, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>2:
						return 'True'
					elif obj[1]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>2.0:
				return 'False'
			else: return 'False'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
