def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.684, "depth": 2}
		if obj[6]<=3.0:
			# {"feature": "Distance", "instances": 21, "metric_value": 0.5917, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Education", "instances": 20, "metric_value": 0.469, "depth": 4}
				if obj[3]>1:
					# {"feature": "Bar", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4138, "depth": 6}
						if obj[8]<=0:
							return 'True'
						elif obj[8]>0:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]>6:
								return 'True'
							elif obj[4]<=6:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]>1.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[9]>2:
				return 'False'
			else: return 'False'
		elif obj[6]>3.0:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 2}
		if obj[2]<=2:
			return 'False'
		elif obj[2]>2:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
