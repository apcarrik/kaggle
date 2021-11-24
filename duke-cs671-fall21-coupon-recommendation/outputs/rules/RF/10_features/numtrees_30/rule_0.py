def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[2]>0:
		# {"feature": "Direction_same", "instances": 31, "metric_value": 0.8238, "depth": 2}
		if obj[8]<=0:
			# {"feature": "Bar", "instances": 23, "metric_value": 0.9321, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Distance", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[9]<=2:
					# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[4]<=6:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[0]>1:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=1:
									return 'False'
								elif obj[3]>1:
									return 'True'
								else: return 'True'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					elif obj[4]>6:
						# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[3]>1:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1.0:
								return 'True'
							elif obj[6]>1.0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=2:
									return 'False'
								elif obj[1]>2:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[3]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]>2:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		elif obj[8]>0:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
