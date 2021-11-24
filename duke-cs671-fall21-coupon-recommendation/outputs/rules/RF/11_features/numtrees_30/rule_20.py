def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[3]>1:
		# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[5]<=12:
				# {"feature": "Distance", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[10]>1:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[7]>1.0:
							# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[4]<=3:
								return 'False'
							elif obj[4]>3:
								return 'True'
							else: return 'True'
						elif obj[7]<=1.0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>1:
								return 'True'
							elif obj[2]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]>1.0:
						# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[1]<=2:
								return 'True'
							elif obj[1]>2:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2]<=3:
									return 'True'
								elif obj[2]>3:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[10]<=1:
					return 'True'
				else: return 'True'
			elif obj[5]>12:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[3]<=1:
		# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[7]>0.0:
			return 'True'
		elif obj[7]<=0.0:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>3:
				return 'False'
			elif obj[1]<=3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
