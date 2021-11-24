def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[6]>0.0:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[4]<=12:
				# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[8]<=0:
						return 'False'
					elif obj[8]>0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]>1.0:
								return 'True'
							elif obj[7]<=1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>12:
				return 'True'
			else: return 'True'
		elif obj[6]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=2:
				return 'False'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
