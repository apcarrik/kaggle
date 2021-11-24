def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]<=14:
		# {"feature": "Distance", "instances": 21, "metric_value": 0.9852, "depth": 2}
		if obj[9]>1:
			# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Coupon", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]<=0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=0:
								return 'True'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[2]>2:
					return 'True'
				else: return 'True'
			elif obj[7]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[9]<=1:
			# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[6]<=2.0:
				return 'True'
			elif obj[6]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]>14:
		return 'False'
	else: return 'False'
