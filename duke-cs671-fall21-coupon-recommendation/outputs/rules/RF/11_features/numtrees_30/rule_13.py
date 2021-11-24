def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 27, "metric_value": 0.9751, "depth": 2}
		if obj[5]>1:
			# {"feature": "Passanger", "instances": 24, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coupon", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[3]<=4:
							# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]>-1.0:
										return 'True'
									elif obj[6]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[7]>1.0:
									return 'False'
								else: return 'False'
							elif obj[4]>3:
								return 'True'
							else: return 'True'
						elif obj[3]>4:
							return 'True'
						else: return 'True'
					elif obj[8]>1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[5]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
