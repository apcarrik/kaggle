def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]>0:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[4]<=10:
			# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=0.0:
						# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[1]<=1:
							return 'True'
						elif obj[1]>1:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>1.0:
								return 'True'
							elif obj[6]<=1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]>0.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]>0:
					return 'False'
				else: return 'False'
			elif obj[3]>2:
				return 'True'
			else: return 'True'
		elif obj[4]>10:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
