def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[1]>0:
			# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[8]<=1:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[4]<=7:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[6]>-1.0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]>0:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=1.0:
								return 'True'
							elif obj[5]>1.0:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0.0:
								return 'False'
							elif obj[5]>0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[4]>7:
					return 'True'
				else: return 'True'
			elif obj[8]>1:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]>1:
					return 'False'
				elif obj[4]<=1:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=1:
						return 'True'
					elif obj[2]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[8]<=2:
				return 'False'
			elif obj[8]>2:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=0:
					return 'False'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 2}
		if obj[4]<=10:
			return 'True'
		elif obj[4]>10:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]>2:
				return 'True'
			elif obj[3]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
