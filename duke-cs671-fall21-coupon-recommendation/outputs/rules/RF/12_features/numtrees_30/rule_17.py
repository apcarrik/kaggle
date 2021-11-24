def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.874, "depth": 1}
	if obj[5]<=2:
		# {"feature": "Bar", "instances": 27, "metric_value": 0.951, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[6]<=12:
				# {"feature": "Coupon", "instances": 21, "metric_value": 0.9587, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[8]<=2.0:
							# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[4]>2:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[9]<=1.0:
									return 'True'
								elif obj[9]>1.0:
									return 'False'
								else: return 'False'
							elif obj[4]<=2:
								return 'True'
							else: return 'True'
						elif obj[8]>2.0:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[2]>3:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[11]<=1:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>0:
								# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]<=1.0:
									return 'False'
								elif obj[8]>1.0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[11]>1:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[6]>12:
				return 'False'
			else: return 'False'
		elif obj[7]>2.0:
			return 'True'
		else: return 'True'
	elif obj[5]>2:
		return 'True'
	else: return 'True'
