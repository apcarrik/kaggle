def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[4]>4:
		# {"feature": "Direction_same", "instances": 22, "metric_value": 0.976, "depth": 2}
		if obj[8]<=0:
			# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 3}
			if obj[1]>0:
				# {"feature": "Education", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[0]>2:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=1.0:
									return 'False'
								elif obj[6]>1.0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[0]<=2:
							return 'False'
						else: return 'False'
					elif obj[7]>1.0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[5]<=1.0:
					return 'True'
				elif obj[5]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]>0:
			return 'True'
		else: return 'True'
	elif obj[4]<=4:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[2]<=3:
			return 'True'
		elif obj[2]>3:
			# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[9]<=1:
				return 'True'
			elif obj[9]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
