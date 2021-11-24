def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[5]<=8:
			# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[7]<=3.0:
				# {"feature": "Passanger", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[3]>0:
						# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[2]>1:
								return 'False'
							elif obj[2]<=1:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[9]>0:
										return 'False'
									elif obj[9]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]>2:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]>2.0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[8]<=2.0:
						return 'True'
					elif obj[8]>2.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>3.0:
				return 'True'
			else: return 'True'
		elif obj[5]>8:
			# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[8]>-1.0:
				return 'False'
			elif obj[8]<=-1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
