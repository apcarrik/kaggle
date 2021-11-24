def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[6]<=3.0:
		# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3]>4:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						elif obj[3]<=4:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[7]>2.0:
				return 'True'
			else: return 'True'
		elif obj[8]>1.0:
			# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[6]>3.0:
		return 'False'
	else: return 'False'
