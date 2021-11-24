def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]<=3:
		# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[8]<=3.0:
			# {"feature": "Time", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[9]<=1.0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[11]>1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]>1:
								# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=16:
									return 'False'
								elif obj[6]>16:
									return 'True'
								else: return 'True'
							elif obj[5]<=1:
								return 'True'
							else: return 'True'
						elif obj[11]<=1:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[9]>1.0:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[8]>3.0:
			return 'True'
		else: return 'True'
	elif obj[4]>3:
		# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
