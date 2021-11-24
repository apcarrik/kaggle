def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[9]<=0:
		# {"feature": "Coupon", "instances": 18, "metric_value": 1.0, "depth": 2}
		if obj[2]>0:
			# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Passanger", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[10]>1:
						# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[1]<=2:
							return 'False'
						elif obj[1]>2:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=1:
								return 'True'
							elif obj[3]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[10]<=1:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[7]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[9]>0:
		return 'True'
	else: return 'True'
