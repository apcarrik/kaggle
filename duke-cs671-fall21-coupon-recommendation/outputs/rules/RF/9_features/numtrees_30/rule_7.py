def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]>0:
		# {"feature": "Education", "instances": 30, "metric_value": 0.8813, "depth": 2}
		if obj[3]>0:
			# {"feature": "Time", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[4]<=7:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[8]<=2:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[0]<=2:
								return 'False'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[8]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'True'
					else: return 'True'
				elif obj[4]>7:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=0:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
