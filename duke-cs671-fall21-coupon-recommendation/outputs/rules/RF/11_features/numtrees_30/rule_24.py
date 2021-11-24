def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[5]>2:
			# {"feature": "Time", "instances": 23, "metric_value": 0.9321, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Coupon", "instances": 20, "metric_value": 0.8113, "depth": 4}
				if obj[2]>2:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[9]<=0:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[4]>2:
								# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=1.0:
									return 'True'
								elif obj[7]>1.0:
									return 'False'
								else: return 'False'
							elif obj[4]<=2:
								return 'False'
							else: return 'False'
						elif obj[9]>0:
							return 'True'
						else: return 'True'
					elif obj[8]>1.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[5]<=2:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
