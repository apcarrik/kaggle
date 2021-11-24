def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[5]<=7:
		# {"feature": "Bar", "instances": 35, "metric_value": 0.8631, "depth": 2}
		if obj[6]<=1.0:
			# {"feature": "Age", "instances": 26, "metric_value": 0.9612, "depth": 3}
			if obj[3]>0:
				# {"feature": "Coupon", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[2]>2:
					# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[1]>0:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[8]<=1.0:
								return 'True'
							elif obj[8]>1.0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=0:
									return 'True'
								elif obj[0]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]>1.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=2:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[1]>2:
						# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[7]>0.0:
							# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[10]>1:
									return 'True'
								elif obj[10]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[7]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[6]>1.0:
			return 'True'
		else: return 'True'
	elif obj[5]>7:
		# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[10]>1:
				# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]>2:
					return 'False'
				elif obj[3]<=2:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]<=1:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[7]>2.0:
			return 'False'
		else: return 'False'
	else: return 'False'
