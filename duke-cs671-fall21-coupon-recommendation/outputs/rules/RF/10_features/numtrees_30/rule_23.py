def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Direction_same", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[8]<=0:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.7973, "depth": 2}
		if obj[2]>2:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.3534, "depth": 3}
			if obj[4]>0:
				return 'True'
			elif obj[4]<=0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=2:
			# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[0]>1:
					# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>2:
							return 'False'
						elif obj[1]<=2:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0.0:
								return 'True'
							elif obj[5]>0.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]>0:
		return 'False'
	else: return 'False'
